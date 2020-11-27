import json


# class Block():

#     def __init__(self, json_block):
#         self.id = json_block['ID']
#         self.name = json_block['Name']
#         self.texture = json_block['Texture']
#         self.props = json_block['Properties']


def main():
    with open('../srcs/data.json') as f:
        d = json.load(f)
        print(type(d))

    # b = Block(d)
    # print(b.id, b.name, b.texture, b.props)


if __name__ == '__main__':
    main()
