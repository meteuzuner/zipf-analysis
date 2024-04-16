import pandas as pd
import matplotlib.pyplot as plt
import argparse

def main(args):
    df = pd.read_csv(args.infile, header=None, names=('word', 'word_frequency'))
    df['rank'] = df['word_frequency'].rank(ascending=False, method='max')
    df['inverse_rank'] = 1 / df['rank']
    ax = df.plot.scatter(x='word_frequency', y='inverse_rank', figsize=[12, 6], grid=True, xlim=args.xlim)
    plt.show()
    
if __name__ == '__main__': 
	parser = argparse.ArgumentParser(description=("Scatter plot for counts"))
	parser.add_argument('infile', type=argparse.FileType('r'), nargs='?', default='-', help='File name')
	parser.add_argument('--xlim', type=int, default=None, help='xlim for matplotlib plot')
	parser.add_argument('--outfile', type=str, default='plotcounts.png', help='Output image file name')
	args = parser.parse_args()
	main(args)