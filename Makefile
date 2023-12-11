install:
    @echo "Installing dependencies..."
    pip install --upgrade pip &&\
        pip install -r requirements.txt
    @echo "Installation complete."

test:
    @echo "Running tests..."
    pytest
    @echo "Tests complete."