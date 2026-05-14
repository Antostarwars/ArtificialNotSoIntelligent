FEATURES = 5
THRESHOLD = 0.5

def activation(x: float) -> int:
    if x > THRESHOLD:
        return 1
    else:
        return 0

def carica_pesi(filename: str):
    weights = []
    
    try:
        with open(filename, "r") as file:
            for i in range(FEATURES):
                line = file.readline().strip()
                if line.startswith("Peso"):
                    try:
                        val = float(line.split(':')[1].strip())
                        weights.append(val)
                    except (IndexError, ValueError):
                        print(f"Errore nella lettura del peso {i}")
                        return False, None, None
                else:
                    print(f"Errore nella lettura del peso {i}")
                    return False, None, None
            
            line = file.readline().strip()
            if line.startswith("Bias:"):
                try:
                    bias = float(line.split(':')[1].strip())
                except (IndexError, ValueError):
                    print("Errore nella lettura del bias")
                    return False, None, None
            else:
                print("Errore nella lettura del bias")
                return False, None, None

            return True, weights, bias

    except FileNotFoundError:
        print(f"Errore: file {filename} non trovato!")
        return False, None, None
    except Exception as e:
        print(f"Errore imprevisto: {e}")
        return False, None, None

def prevedi(weights: list, bias: float, input_data: list) -> int:
    if len(weights) != FEATURES or len(input_data) != FEATURES:
        raise ValueError(f"Attesi {FEATURES} pesi e {FEATURES} input.")

    somma = bias + sum(w * i for w, i in zip(weights, input_data))
    
    return activation(somma)