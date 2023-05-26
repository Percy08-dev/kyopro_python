import decimal
def main():
    x = input()
    print(decimal.Decimal(x).quantize(decimal.Decimal("0"), rounding=decimal.ROUND_HALF_UP))

if __name__ == "__main__":
    main()