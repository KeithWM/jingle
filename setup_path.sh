# Usage source FILENAME_OF_THIS_FILE
LIB_DIR=$(cd lib; pwd)
#See https://stackoverflow.com/questions/33615156/why-does-pythonpath-with-trailing-colon-add-current-directory-to-sys-path
export PYTHONPATH="LIB_DIR{PYTHONPATH+":"}${PYTHONPATH-}"
