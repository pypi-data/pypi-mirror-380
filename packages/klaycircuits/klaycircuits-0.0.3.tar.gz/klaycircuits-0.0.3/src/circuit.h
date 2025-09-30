#pragma once

#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <nanobind/stl/pair.h>
#include <nanobind/stl/vector.h>
#include <nanobind/ndarray.h>
#include <nanobind/operators.h>

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <list>
#include <cstdint>

#include "node.h"
#include "hash_set8.hpp"

namespace nb = nanobind;
using namespace nb::literals;

typedef std::vector<nb::ndarray<nb::numpy, long int, nb::shape<-1>>> Arrays;


class NodePtr {
public:
    NodePtr(Node* ptr) : ptr(ptr) { }

    Node* get() const {
        return ptr;
    }

    std::string to_string() const {
        std::stringstream ss;
        ss << "NodePtr(" << this->as_int() << ")";
        return ss.str();
    }

    bool operator==(NodePtr other) const {
        return this->ptr == other.ptr;
    }

    std::uintptr_t as_int() const {
        return reinterpret_cast<std::uintptr_t>(ptr);
    }

private:
    Node* ptr;
};


class Circuit {

public:
    // Circuit representation as a Merkle DAG
    std::vector<emhash8::HashSet<Node*, NodeHash, NodeEqual>> layers;
    // Root nodes in order they were added to the Circuit
    std::vector<Node*> roots = {};

    ~Circuit() {
        for (auto& layer: layers) {
            for (auto& node: layer)
                delete node;
            layer.clear();
        }
    }

private:

    /**
     * Add the given node to the circuit.
     *
     * Beware! This does not add intermediate nodes to intermediate layers.
     * Please use add_node_level instead.
     *
     * Uses node->layer to consider the correct layer of the circuit.
     * After adding a node, the Circuit assumes ownership and will free it upon deletion.
     * If the given node was equal to one already present, the given node is freed (deleted),
     * and the already found node is returned.
     *
     * This will update node->ix.
     *
     * @param node The node to add.
     * @return If no equivalent node was present yet, returns the node itself and true.
     * If there was already an equivalent node present, returns a pointer to that node, and false.
     */
    Node* add_node(Node* node);

    /**
     *  Moves all roots to a new layer at the top of the circuit.
     */
    void add_root_layer();

public:
    void set_root(NodePtr root) {
        Node* root_cast = static_cast<Node *>(root.get());
        roots.push_back(root_cast);
    }

    /**
     * Add node to this circuit and ensure each child is in the previous adjacent layer.
     *
     * If a child does not exist in the previous layer, a chain of dummy nodes will be added in between.
     * Uses node->layer to consider the correct layer of the circuit.
     * After adding a node, the Circuit assumes ownership and will free it upon deletion.
     *
     * This may change node->children and will update node->ix.
     *
     * Importantly, we assume that the children are already part of the circuit.
     * For this reason we also return a pair, if an equivalent node (but different instance!)
     * was already present, we simply return that node and free (delete) the given node)
     *
     * @param node The new node to add to the circuit. May be freed (deleted).
     * @return If no equivalent node was present yet, returns the node itself and true.
     * If there was already an equivalent node present, returns a pointer to that node, and false.
     */
    Node* add_node_level(Node* node);

    /**
     * The same as `add_node_level`, but it compresses the given node first.
     *
     * If node is an OR node: any child that is False is removed.
     * If node is an OR node: if any child is a True Node, the returned node is True.
     * If node is an AND node: any child that is True is removed.
     * If node is an AND node: if any child is a False Node, the returned node is False.
     *
     * This means some child nodes may never be used.
     * Therefore, after construction, we advise to run
     * `remove_unused_nodes()`
     *
     */
    Node* add_node_level_compressed(Node* node);

    /**
     * Get the corresponding node in the circuit.
     * This may be a different node instance with the same hash and
     * is equal according to the `NodeEqual` struct.
     */
    Node* get_node(Node* node) { return *(layers[node->layer].find(node)); }

    /**
     * Number of layers in this circuit.
     */
    inline std::size_t nb_layers() const { return layers.size(); }

    /**
     * Maximum layer width in this circuit.
     */
    std::size_t max_layer_width() const;

    NodePtr add_sdd_from_file(const std::string &filename, std::vector<int>& true_lits, std::vector<int>& false_lits);

    NodePtr add_d4_from_file(const std::string &filename, std::vector<int>& true_lits, std::vector<int>& false_lits);

    /**
     * Remove all nodes from this circuit that are not used.
     *
     * If a non-input, non-root node is not the child of another node,
     * it is removed in-place.
     */
    void remove_unused_nodes();

    std::pair<Arrays, Arrays> get_indices();

    /**
     * Number of nodes in the whole circuit.
     */
    std::size_t nb_nodes() const {
        std::size_t count = 0;
        for (const auto &layer: layers)
            count += layer.size();
        return count;
    }

    std::size_t nb_root_nodes() const {
        return roots.size();
    }

    /**
     * For debugging purposes;
     * prints every node of each layer
     */
    void print_circuit() const {
        for (const auto &layer : layers) {
            std::cout << "--- next layer ---" << std::endl;
            for (const auto &node : layer) {
                std::cout << node->get_label() << " connects to ";
                for (const auto &child : node->children) {
                    std::cout << child->get_label() << ",";
                }
                std::cout << std::endl;
            }
            std::cout << std::endl;
        }
    }

    NodePtr true_node() {
        Node* node = Node::createTrueNode();
        return NodePtr(add_node_level_compressed(node));
    }

    NodePtr false_node() {
        Node* node = Node::createFalseNode();
        return NodePtr(add_node_level_compressed(node));
    }

    NodePtr literal_node(int lit) {
      	if (lit == 0) {
        	throw domain_error("literal_node(lit) does not allow lit == 0, because negation -0 does not make sense.");
        }
        Node* node = Node::createLiteralNode(Lit::fromInt(lit));
        return NodePtr(add_node_level_compressed(node));
    }

    NodePtr and_node(std::vector<NodePtr> children) {
        Node* node = Node::createAndNode();
        for (auto child: children) {
            Node *child_cast = child.get();
            node->add_child(child_cast);
        }
        return NodePtr(add_node_level_compressed(node));
    }

    NodePtr or_node(std::vector<NodePtr> children) {
        Node* node = Node::createOrNode();
        for (auto child: children) {
            Node *child_cast = child.get();
            node->add_child(child_cast);
        }
        return NodePtr(add_node_level_compressed(node));
    }
};
