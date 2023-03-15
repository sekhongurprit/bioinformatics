#! /usr/bin/python
import sys
import pandas as pd
import argparse
def main():
    parser=argparse.ArgumentParser(description='Combine two columns of csv files to a new csv file')
    parser.add_argument("-f1", "--file1", metavar="", type=str, required=True, help="First File[To be sorted before combining]")
    parser.add_argument("-f2", "--file2", metavar="", type=str, required=True, help="Second File ")
    parser.add_argument("-o", "--outfile", metavar="", type=str, required=True, help="Output File Name ")
    group=parser.add_mutually_exclusive_group()
    group.add_argument("-q", "--quite", action='store_true', help="print quite")
    group.add_argument("-v", "--verbose", action='store_true', help="print verbose")
    args=parser.parse_args()
    if args.quite:
        combine(args.file1, args.file2, args.outfile)
    elif args.verbose:
        combine(args.file1, args.file2, args.outfile)
        print("One of the column from %s is sorted and combined with %s, and results is written to %s" %(args.file1, args.file2, args.outfile) )
    else:
        combine(args.file1, args.file2, args.outfile)
        print("Cobined columns are written to: %s" % args.outfile)

def sort(infile):
    df= pd.read_csv(infile, "\s+", names =["frame", "pop"])
    x=0
    data=[]
    counter=0
    for row in df["pop"]:
        counter+=1
        if row>x:
             x+=1
             data.append(df.iloc[counter-1,[0]])
    df=pd.DataFrame(data)  
    df.reset_index(drop=True, inplace=True)
    print(df.head(5))
    return df

def combine(infile1, infile2, outfile):
    df1=pd.DataFrame()
    df3=pd.DataFrame()
    df1=sort(infile1)
    df2=pd.read_csv(infile2, "\s+")
    df2=df2.drop("#Frame", axis=1)
    df1["rms"]=df2["RMSD_00002"]
    #df3=df1.join(df2, on=None)
    df1.to_csv(outfile, sep='\t', index=False, header=False)

if __name__ == "__main__":
    main()
