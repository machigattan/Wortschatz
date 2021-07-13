import sys, json

#Read data from stdin
# def read_in():
#     lines = sys.stdin.readlines()
#     # Since our input would only be having one line, parse our JSON data from that
#     return json.loads(lines)

def main():

        lines = sys.stdin.readlines()
    #get our data as an array from read_in()
    lines = read_in()

    # Sum  of all the items in the providen array
    # total_sum_inArray = 0
    # for item in lines:
    #     total_sum_inArray += item

    #return the sum to the output stream
    print (lines)

# Start process
if __name__ == '__main__':
    main()