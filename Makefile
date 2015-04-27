all: 
	@echo "***** Enumeration 1 Resuls *****" > temp
	python enum1.py
	cat MSS_Results.txt >> temp

	@echo "***** Better Enumeration Resuls *****" >> temp
	python enum2.py
	cat MSS_Results.txt >> temp

	@echo "***** Divide and Conquer Results *****" >> temp
	python Divide_and_Conquer.py
	cat MSS_Results.txt >> temp
	
	@echo "***** Linear Time Resuls *****" >> temp
	python Linear-Time.py 0
	cat MSS_Results.txt >> temp

	cat temp > MSS_Results.txt
