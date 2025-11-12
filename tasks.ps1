function run {
    streamlit run src/energy_ml/main.py
}

function test {
    pytest -q
}

function fmt {
    black src tests
}
