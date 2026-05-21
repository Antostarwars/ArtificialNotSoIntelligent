import percettrone

N = 32
EPOCHS = 500
LEARNING_RATE = 0.1

def train():
    inputs = []
    expected = []

    for i in range(N):
        artista = (i >> 4) & 1
        meteo   = (i >> 3) & 1
        amici   = (i >> 2) & 1
        cibo    = (i >> 1) & 1
        alcool  = i & 1
        
        inputs.append([artista, meteo, amici, cibo, alcool])
        
        if (artista == 1 or amici == 1) and meteo == 1:
            expected.append(1)
        else:
            expected.append(0)

    weights = [0.0] * percettrone.FEATURES
    bias = 0.0

    for epoch in range(EPOCHS):
        for i in range(N):
            sum_val = bias + sum(w * x for w, x in zip(weights, inputs[i]))
            output = percettrone.activation(sum_val)
            error = expected[i] - output
            
            for j in range(percettrone.FEATURES):
                weights[j] += LEARNING_RATE * error * inputs[i][j]
            bias += LEARNING_RATE * error

    print(f"Pesi allenati per il concerto dopo {EPOCHS} epoche:")
    for i in range(percettrone.FEATURES):
        print(f"Peso {i}: {weights[i]:.6f}")
    print(f"Bias: {bias:.6f}\n")

    try:
        with open("pesi_concerto.txt", "w") as file:
            for i in range(percettrone.FEATURES):
                file.write(f"Peso {i}: {weights[i]:.6f}\n")
            file.write(f"Bias: {bias:.6f}\n")
        print("File 'pesi_concerto.txt' aggiornato con successo. Ora puoi eseguire main.py.")
    except IOError as e:
        print(f"Errore di I/O durante il salvataggio del file: {e}")

if __name__ == "__main__":
    train()
