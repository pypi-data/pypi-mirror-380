#!/bin/bash
# Generate Python protobuf files from core protos
# Run this from the api/langgraph_api/grpc_ops directory

set -e

# Get the project root (three levels up from api/langgraph_api/grpc_ops)
PROJECT_ROOT="$(cd ../../../ && pwd)"
PROTO_DIR="${PROJECT_ROOT}/core/protos"
OUTPUT_DIR="generated"

# Check if proto file exists
if [[ ! -f "${PROTO_DIR}/core-api.proto" ]]; then
    echo "Error: Proto file not found at ${PROTO_DIR}/core-api.proto"
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "${OUTPUT_DIR}"

# Generate Python protobuf files
echo "Generating Python protobuf files..."
uv run python -m grpc_tools.protoc \
    -I"${PROTO_DIR}" \
    --python_out="${OUTPUT_DIR}" \
    --grpc_python_out="${OUTPUT_DIR}" \
    --pyi_out="${OUTPUT_DIR}" \
    "${PROTO_DIR}/core-api.proto"

# Fix imports to be relative in the generated gRPC file
echo "Fixing imports to be relative..."
if [[ -f "${OUTPUT_DIR}/core_api_pb2_grpc.py" ]]; then
    # Make import of core_api_pb2 relative, preserving whatever alias grpc_tools chose
    sed -i.bak 's/^import core_api_pb2 as /from . import core_api_pb2 as /' "${OUTPUT_DIR}/core_api_pb2_grpc.py"
    rm -f "${OUTPUT_DIR}/core_api_pb2_grpc.py.bak"
fi

# Create __init__.py files
cat > "${OUTPUT_DIR}/__init__.py" << 'EOF'
# Generated protobuf files
from . import core_api_pb2
from . import core_api_pb2_grpc

__all__ = ["core_api_pb2", "core_api_pb2_grpc"]
EOF

echo "Python protobuf files generated successfully!"
