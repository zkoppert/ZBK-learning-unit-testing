test_file = CalcTest

test: Smoke Operations

.PHONY: test Smoke Operations

Smoke:
	python3 -m unittest $(test_file).CalcTestDummie -v
Operations:
	python3 -m unittest $(test_file).CalcTestOperations -v
