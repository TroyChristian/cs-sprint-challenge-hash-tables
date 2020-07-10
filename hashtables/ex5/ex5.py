# Your code here



def finder(files, queries):
    split_paths = []
    result = []
    for path in files:
        split_paths.append(path.split("/"))

    hash_table = dict(zip(files, split_paths))

    for query in queries:
        for key,value in hash_table.items():
            if query in value:
                result.append(key)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
