def calculate_fee(amount):
	return round(amount * 0.02,2)

	if __name__ == "__main__":
		amount = 1000

	fee = calculate_fee(amount)

	print("Finance service portal")
	print("-------------------------")
	print("transaction Amount: ",amount)
	print("processing Fee: ",fee)
