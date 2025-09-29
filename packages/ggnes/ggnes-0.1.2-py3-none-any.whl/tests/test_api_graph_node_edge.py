"""
Comprehensive tests for Graph, Node, and Edge API expectations.
Tests both what users would naturally try and what actually works.
"""

import os
import sys

import pytest

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ggnes import Edge, Graph, Node, NodeType


class TestNodeCreationAPI:
    """Test all variations of node creation that users might try."""

    def test_node_creation_intuitive_top_level(self):
        """Users naturally put output_size at top level."""
        graph = Graph()
        node_id = graph.add_node(
            {
                "node_type": "input",
                "output_size": 10,  # Intuitive placement
                "activation_function": "relu",
            }
        )
        assert node_id is not None

    def test_node_creation_actual_api(self):
        """Document the actual working API."""
        graph = Graph()
        node_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,  # Must use enum
                "activation_function": "relu",
                "attributes": {"output_size": 10},  # Must be in attributes
            }
        )
        assert node_id == 0  # Auto-assigned integer

    def test_node_creation_with_custom_id(self):
        """Users want to specify meaningful node IDs."""
        graph = Graph()
        node_id = graph.add_node(
            {
                "id": "input_layer",  # Want custom ID
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 784},
            }
        )
        assert node_id == "input_layer"
        # Check node was added with custom ID
        assert graph.get_node("input_layer") is not None

    def test_node_creation_with_string_type(self):
        """Users expect to use string node types."""
        graph = Graph()
        node_id = graph.add_node(
            {
                "node_type": "hidden",  # String, not enum
                "activation_function": "relu",
                "attributes": {"output_size": 32},
            }
        )
        assert node_id is not None

    def test_node_object_direct_creation(self):
        """Test creating Node objects directly."""
        node = Node(
            id="conv1",
            node_type="hidden",
            output_size=32,
            activation_function="relu",
            aggregation_function="sum",
        )
        assert node.custom_id == "conv1"
        assert node.output_size == 32

    def test_node_object_actual_creation(self):
        """Document Node constructor works with wrapper."""
        # Wrapper supports intuitive format
        node = Node(id=0, node_type=NodeType.HIDDEN, activation_function="relu", output_size=32)
        assert node.custom_id == 0
        assert node.output_size == 32

    def test_add_node_object_to_graph(self):
        """Users expect to add Node objects to graph."""
        graph = Graph()
        node = Node(
            id="hidden1", node_type=NodeType.HIDDEN, activation_function="relu", output_size=32
        )
        node_id = graph.add_node(node)
        assert node_id == "hidden1"
        assert graph.get_node("hidden1") is not None


class TestEdgeCreationAPI:
    """Test Edge creation and addition to graphs."""

    def test_edge_creation_intuitive(self):
        """Users expect simple Edge creation."""
        edge = Edge(src_id="input", dst_id="output", weight=0.5)
        assert edge.src_id == "input"
        assert edge.dst_id == "output"

    def test_edge_creation_actual(self):
        """Document Edge constructor works with wrapper."""
        # Wrapper supports both formats
        edge = Edge(src_id=0, dst_id=1, weight=0.5)
        assert edge.src_id == 0
        assert edge.dst_id == 1

    def test_add_edge_object(self):
        """Users expect to add Edge objects."""
        graph = Graph()
        n1 = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )
        n2 = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 1},
            }
        )

        edge = Edge(src_id=n1, dst_id=n2)
        result = graph.add_edge(edge)  # Should accept Edge object

        assert result is not None
        assert len(list(graph.list_edges())) == 1

    def test_add_edge_actual(self):
        """Document actual add_edge API."""
        graph = Graph()
        n1 = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )
        n2 = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 1},
            }
        )

        # Wrapper supports both formats
        edge_id = graph.add_edge(n1, n2)
        assert edge_id is not None

    def test_edge_with_string_ids(self):
        """Users want to use meaningful names in edges."""
        graph = Graph()
        # First create nodes with names
        graph.add_node({"id": "input", "node_type": "input", "output_size": 10})
        graph.add_node({"id": "hidden1", "node_type": "hidden", "output_size": 20})
        graph.add_node({"id": "hidden2", "node_type": "hidden", "output_size": 20})
        graph.add_node({"id": "output", "node_type": "output", "output_size": 1})

        # Then add edges
        graph.add_edge("input", "hidden1")
        graph.add_edge("hidden1", "hidden2")
        graph.add_edge("hidden2", "output")


class TestGraphConstruction:
    """Test various graph construction patterns."""

    def test_intuitive_graph_construction(self):
        """How users would naturally build a graph."""
        graph = Graph()

        # Add nodes with meaningful names
        graph.add_node({"id": "image_input", "type": "input", "size": 784})

        graph.add_node({"id": "conv1", "type": "conv", "filters": 32, "kernel_size": 3})

        graph.add_node({"id": "pool1", "type": "maxpool", "pool_size": 2})

        graph.add_node({"id": "fc1", "type": "dense", "units": 128})

        graph.add_node({"id": "output", "type": "output", "units": 10})

        # Connect with meaningful names
        graph.add_edge("image_input", "conv1")
        graph.add_edge("conv1", "pool1")
        graph.add_edge("pool1", "fc1")
        graph.add_edge("fc1", "output")

        # Should be able to query by name
        conv_node = graph.get_node("conv1")
        assert conv_node is not None
        assert conv_node.attributes.get("filters") == 32
        assert graph.has_edge("conv1", "pool1")

    def test_actual_graph_construction(self):
        """Document how to actually build a graph."""
        graph = Graph()

        # Must use specific format
        input_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 784},
            }
        )

        hidden1_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 128},
            }
        )

        hidden2_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 64},
            }
        )

        output_id = graph.add_node(
            {
                "node_type": NodeType.OUTPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )

        # Connect with integer IDs
        graph.add_edge(input_id, hidden1_id)
        graph.add_edge(hidden1_id, hidden2_id)
        graph.add_edge(hidden2_id, output_id)

        assert len(graph.nodes) == 4
        assert len(list(graph.list_edges())) == 3

    def test_graph_query_methods(self):
        """Users expect graph query capabilities."""
        graph = Graph()

        # Add some nodes
        n1 = graph.add_node({"id": "input", "node_type": "input", "output_size": 10})

        n2 = graph.add_node({"id": "hidden", "node_type": "hidden", "output_size": 20})

        # Add edge to test graph traversal
        graph.add_edge("input", "hidden")

        # Query methods users would expect
        input_node = graph.get_node("input")
        assert input_node is not None
        assert input_node.attributes.get("output_size") == 10

        hidden_nodes = graph.get_node_by_type("hidden")
        assert "hidden" in hidden_nodes

        predecessors = graph.get_predecessors("hidden")
        assert "input" in predecessors

        successors = graph.get_successors("input")
        assert "hidden" in successors

        path = graph.get_path("input", "hidden")
        assert path == ["input", "hidden"]


class TestGraphValidation:
    """Test graph validation and error messages."""

    def test_missing_output_size_error(self):
        """Wrapper provides default output_size when missing."""
        graph = Graph()

        # Wrapper handles missing output_size gracefully by providing defaults
        node_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                # Missing output_size - wrapper provides default
            }
        )

        # Should succeed with default value
        assert node_id is not None
        node = graph.get_node(node_id)
        assert node.attributes.get("output_size") == 10  # Default for INPUT

    def test_wrong_output_size_location_error(self):
        """Wrapper accepts output_size at top level (intuitive)."""
        graph = Graph()

        # Wrapper handles output_size at top level correctly
        node_id = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "output_size": 10,  # Wrapper accepts this
            }
        )

        # Should succeed
        assert node_id is not None
        node = graph.get_node(node_id)
        assert node.attributes.get("output_size") == 10

    def test_invalid_node_reference_error(self):
        """Error should be clear when referencing non-existent nodes."""
        graph = Graph()

        n1 = graph.add_node(
            {"node_type": NodeType.INPUT, "activation_function": "linear", "output_size": 10}
        )

        with pytest.raises(Exception) as exc_info:
            graph.add_edge(n1, 999)  # Non-existent

        error_msg = str(exc_info.value)
        # Should mention node 999 doesn't exist
        assert (
            "999" in error_msg
            or "not found" in error_msg.lower()
            or "not exist" in error_msg.lower()
        )


class TestNodeAttributes:
    """Test node attribute handling."""

    def test_all_node_attributes(self):
        """Test all possible node attributes."""
        graph = Graph()

        node_id = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {
                    "output_size": 32,
                    "aggregation_function": "sum",
                    "dropout_rate": 0.5,
                    "use_bias": True,
                    "kernel_initializer": "glorot_uniform",
                    "custom_param": "test",
                },
            }
        )

        node = graph.nodes[node_id]
        assert node.attributes["output_size"] == 32
        assert node.attributes["aggregation_function"] == "sum"
        assert node.attributes.get("dropout_rate") == 0.5

    @pytest.mark.xfail(reason="No attribute validation")
    def test_attribute_validation(self):
        """Attributes should be validated."""
        graph = Graph()

        with pytest.raises(ValueError) as exc_info:
            graph.add_node(
                {
                    "node_type": NodeType.HIDDEN,
                    "activation_function": "invalid_activation",  # Invalid
                    "attributes": {"output_size": 32},
                }
            )

        assert "activation" in str(exc_info.value).lower()

        with pytest.raises(ValueError) as exc_info:
            graph.add_node(
                {
                    "node_type": NodeType.HIDDEN,
                    "activation_function": "relu",
                    "attributes": {
                        "output_size": -10  # Invalid
                    },
                }
            )

        assert "positive" in str(exc_info.value).lower()


class TestGraphModification:
    """Test graph modification operations."""

    def test_remove_node(self):
        """Should be able to remove nodes."""
        graph = Graph()

        n1 = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )

        n2 = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 20},
            }
        )

        graph.add_edge(n1, n2)

        # Should be able to remove node
        graph.remove_node(n2)
        assert graph.get_node(n2) is None
        # Edge should also be removed
        assert not graph.has_edge(n1, n2)

    def test_remove_edge(self):
        """Should be able to remove edges."""
        graph = Graph()

        n1 = graph.add_node(
            {
                "node_type": NodeType.INPUT,
                "activation_function": "linear",
                "attributes": {"output_size": 10},
            }
        )

        n2 = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 20},
            }
        )

        graph.add_edge(n1, n2)

        # Should be able to remove edge by specifying endpoints
        graph.remove_edge(n1, n2)
        assert not graph.has_edge(n1, n2)

    def test_modify_node_attributes(self):
        """Should be able to modify node attributes."""
        graph = Graph()

        n1 = graph.add_node(
            {
                "node_type": NodeType.HIDDEN,
                "activation_function": "relu",
                "attributes": {"output_size": 32},
            }
        )

        # Should be able to modify
        graph.modify_node(n1, {"activation_function": "tanh", "attributes": {"output_size": 64}})

        node = graph.get_node(n1)
        assert node.activation_function == "tanh"
        assert node.attributes["output_size"] == 64
