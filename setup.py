from distutils.core import setup

setup(
    name='StockAnalysis',
    version='0.2.1',
    description='Classes for technical analysis of stocks.',
    author='Ayush Anand',
    author_email='ayush100anand@gmail.com',
    license='MIT',
    url='https://github.com/INVIII/StockAnalysis',
    packages=['stock_analysis'],
    install_requires=[
        'matplotlib>=3.0.2',
        'mplfinance>=0.12.7a4',
        'numpy>=1.15.2',
        'pandas>=0.23.4',
        'pandas-datareader>=0.7.0',
        'seaborn>=0.11.0',
        'statsmodels>=0.11.1',
        'yfinance>=0.2.4'
    ],
)
