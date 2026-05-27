"""Module providing main function."""
import argparse
from loan.eligibility import evaluate, format_report


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--income", type=float, required=True)
    p.add_argument("--debt", type=float, required=True)
    p.add_argument("--tenure-months", type=int, required=True)
    p.add_argument("--age", type=int, required=True)
    p.add_argument("--savings-balance", type=float, required=True)
    p.add_argument("--late-payments", type=int, default=0)
    p.add_argument("--dependents", type=int, default=0)
    p.add_argument("--name", type=str, default="Member")
    a = p.parse_args()
    r = evaluate(a.income, a.debt, a.tenure_months, a.age, a.savings_balance, a.late_payments, a.dependents)
    print(format_report(r, a.name))


if __name__ == "__main__":
    main()
