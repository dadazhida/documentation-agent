import argparse
from app.services.doc_generator import generate_document

def main():
    parser = argparse.ArgumentParser(description="要件定義書生成CLI")
    parser.add_argument("--task", type=str, required=True, help="作成したいプロダクト案")
    parser.add_argument("--k", type=int, default=5, help="主要機能の最小数")
    args = parser.parse_args()

    result = generate_document(args.task, args.k)
    print(result)

if __name__ == "__main__":
    main()