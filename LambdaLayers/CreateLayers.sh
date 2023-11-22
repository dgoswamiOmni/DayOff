#!/bin/bash

# Inputs
REQUIREMENTS_TXT_PATH="requirements.txt"

# Directories
TMP_DIR="tmp"
LAYERS_DIR="layers"

# Layer information
LAYER_NAME="python_lib_layer"
LAYER_DESC="Python library layer for AWS Lambda"

# Clean up and create directories
rm -rf ${TMP_DIR} ${LAYERS_DIR}
mkdir -p ${TMP_DIR} ${LAYERS_DIR}

# Install libraries to temporary directory
pip install -r ${REQUIREMENTS_TXT_PATH} -t ${TMP_DIR}

# Zip the temporary directory to create the layer
cd ${TMP_DIR}
zip -r ../${LAYERS_DIR}/${LAYER_NAME}.zip .

# Clean up the temporary directory
cd ..
rm -rf ${TMP_DIR}

# Upload the layer to AWS Lambda
# aws lambda publish-layer-version \
#     --layer-name ${LAYER_NAME} \
#     --description "${LAYER_DESC}" \
#     --zip-file fileb://${LAYERS_DIR}/${LAYER_NAME}.zip \
#     --compatible-runtimes python3.6 python3.7 python3.8