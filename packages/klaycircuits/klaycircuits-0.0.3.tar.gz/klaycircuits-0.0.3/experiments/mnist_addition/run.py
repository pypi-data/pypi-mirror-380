import argparse
from collections import defaultdict
from functools import reduce
from time import perf_counter

import numpy as np
import torch
from pysdd.sdd import SddManager, Vtree
import klay
from tqdm import tqdm
import torch.nn as nn
from torchvision.datasets import MNIST
import torchvision.transforms as transforms


def get_circuit(nb_digits: int):
    """
    Generate a multi-rooted circuit that computes the sum of two numbers of `nb_digits` digits.
    Note: this would typically be the end product of a higher-level language such as DeepProbLog,
    but here we construct the circuit manually to keep the code self-contained.
    """
    circuit = klay.Circuit()
    vtree = Vtree(var_count=20 * nb_digits, vtree_type="balanced")
    manager = SddManager.from_vtree(vtree)

    sdds = defaultdict(manager.false)
    for n1 in tqdm(range(10**nb_digits)):
        for n2 in range(10**nb_digits):
            model = [~manager.l(i+1) for i in range(20 * nb_digits)]
            n1_digits = map(int, f"{n1:0{nb_digits}d}")
            n2_digits = map(int, f"{n2:0{nb_digits}d}")
            n1_vars = [x + i*10 for i, x in enumerate(n1_digits)]
            n2_vars = [x + i*10 + nb_digits*10 for i, x in enumerate(n2_digits)]
            for v in n1_vars + n2_vars:
                model[v] = manager.l(v+1)
            sdds[n1+n2] |= reduce(lambda x, y: x & y, model)

    for sdd in tqdm(sdds.values()):
        circuit.add_sdd(sdd)
    print("Nb nodes", circuit.nb_nodes())
    return circuit


def get_dataloader(nb_digits: int, batch_size: int, train: bool = True):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,)),
    ])
    dataset = MNIST('data', train=train, download=True, transform=transform)
    return torch.utils.data.DataLoader(
        dataset,
        batch_size=nb_digits*2 * batch_size,
        shuffle=train,
        num_workers=2,
        pin_memory=True,
    )


class LeNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 6, 5),
            nn.MaxPool2d(2, 2),
            nn.ReLU(),
            nn.Conv2d(6, 16, 5),
            nn.MaxPool2d(2, 2),
            nn.ReLU(),
        )
        self.classifier = nn.Sequential(
            nn.Linear(16 * 4 * 4, 120),
            nn.ReLU(),
            nn.Linear(120, 84),
            nn.ReLU(),
            nn.Linear(84, 10),
        )
        self.activation = torch.nn.LogSoftmax(dim=-1)

    def forward(self, x):
        x = self.encoder(x)
        x = x.view(-1, 16 * 4 * 4)
        x = self.classifier(x)
        return self.activation(x)


class MnistAdditionModule(nn.Module):
    def __init__(self, nb_digits: int):
        super().__init__()
        self.net = LeNet()
        self.circuit = get_circuit(nb_digits).to_torch_module()
        self.circuit_batched = torch.compile(torch.vmap(self.circuit), mode='reduce-overhead')
        self.nb_digits = nb_digits

    def forward(self, images):
        image_probs = self.net(images)  # (batch_size*2*nb_digits, 10)
        batch_size = image_probs.shape[0] // (2*self.nb_digits)
        image_probs = image_probs.reshape(batch_size, -1) # (batch_size, 2*nb_digits*10)
        zeros = torch.zeros_like(image_probs)
        return self.circuit_batched(image_probs, zeros)


def to_label(ys, nb_digits: int):
    ys = ys.reshape(-1, 2*nb_digits)
    exponents = 10 ** torch.arange(start=nb_digits-1, end=-1, step=-1, device=ys.device).repeat(2)
    return (ys * exponents).sum(dim=1)


def main(nb_digits: int, learning_rate: float, batch_size: int, nb_epochs: int, device: str):
    dataloader = get_dataloader(nb_digits, batch_size)
    model = MnistAdditionModule(nb_digits).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate, weight_decay=10e-6)

    epoch_times = []
    for epoch in range(nb_epochs):
        print(f"### Epoch {epoch+1} ###")
        losses = []
        t1 = perf_counter()
        for xs, ys in dataloader:
            xs, ys = xs.to(device), ys.to(device)
            preds = model(xs)
            labels = to_label(ys, nb_digits)
            loss = nn.functional.nll_loss(preds, labels)
            losses.append(loss.item())
            assert not torch.isnan(loss).any()
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

        epoch_times.append(perf_counter() - t1)
        print(f"Epoch {epoch}, Loss {np.mean(losses):.5f} ({epoch_times[-1]:.2f}s)")

    print(f"Mean epoch time {np.mean(epoch_times[2:]):.2f} \\pm {np.std(epoch_times[2:]):.2f}")

    dataloader = get_dataloader(nb_digits, batch_size, train=False)
    correct = []
    for xs, ys in dataloader:
        xs, ys = xs.to(device), ys.to(device)
        labels = to_label(ys, nb_digits)
        preds = model(xs).argmax(dim=-1)
        correct += (preds == labels).tolist()
    print("Accuracy", np.mean(correct))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--nb_digits', type=int, default=2)
    parser.add_argument('-b', '--batch_size', type=int, default=128)
    parser.add_argument('-e', '--nb_epochs', type=int, default=12)
    parser.add_argument('-d', '--device', default='cpu')
    parser.add_argument('-lr', '--learning_rate', type=float, default=0.0003)
    args = parser.parse_args()

    main(args.nb_digits, args.learning_rate, args.batch_size, args.nb_epochs, args.device)

