cat > test_installation.py << 'EOF'
from currency_rates_cbr import CurrencyController, CurrencyView

# Тестируем основной функционал
controller = CurrencyController(["USD", "EUR", "CNY"])
rates = controller.get_current_rates()

print("=== Текстовый формат ===")
print(CurrencyView.display_rates(rates))

print("\n=== JSON формат ===")
print(CurrencyView.display_json(rates))

print("\n=== Тест синглтона ===")
from currency_rates_cbr import CurrencyRates
model1 = CurrencyRates()
model2 = CurrencyRates()
print(f"Это один и тот же объект: {model1 is model2}")
EOF