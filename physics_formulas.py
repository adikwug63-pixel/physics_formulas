print("Physics Formulas")

print("A. a = Δv / Δt")
print("B. a = F / m")
print("C. a = v² / r")
print("D. a = g sin(θ)")
print("E. a = (v - u) / t")

choice = input("Enter your choice (A-E): ")

formulas = {
    "A": "a = Δv / Δt",
    "B": "a = F / m",
    "C": "a = v² / r",
    "D": "a = g sin(θ)",
    "E": "a = (v - u) / t",
}

print(formulas[choice.upper()])
