# Total Oil Check - My First Project
print("=== TOTAL OIL CHECK ===")

total_oil = float(input("Total Oil (litre me) daalo: "))
used_oil = float(input("Kitna Oil Use hua? : "))
remaining = total_oil - used_oil

print("------------------------")
print(f"Total Oil: {total_oil} Litre")
print(f"Used Oil: {used_oil} Litre")
print(f"Bacha hua Oil: {remaining} Litre")

if remaining < 5:
    print("⚠️ WARNING: Oil khatam hone wala hai! Naya mangwao!")
elif remaining < 10:
    print("Thoda bacha hai, dhyan rakho!")
else:
    print("✅ Oil kaafi hai! Tension mat lo!")
print("------------------------")
print("Made by jaymanchekar29-tech")
