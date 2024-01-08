from revenue_analyser import RevenueAnalyzer

def test_load_data():
    analyzer = RevenueAnalyzer('orders.csv')
    assert analyzer.load_data() == True

def test_load_data_file_not_found():
    analyzer = RevenueAnalyzer('nonexistent.csv')
    assert analyzer.load_data() == False