def create_tag(tag_name, tag_content):
    return f"<{tag_name}>{tag_content}</{tag_name}>"


def create_row(row_data, cell_tag):
    row_content = ""
    for cell in row_data:
        if cell is None:
            cell = ""
        row_content += create_tag(cell_tag, cell)
        
    return row_content


# [[1, 3, 4], [2, 4, 4]]


def to_table(table_data, header=False, index=False):
    
    header_content = ""
    if header:
        if index: 
            header_content += create_tag("th", "") 
        header_data = table_data[0]
        header_content += create_row(header_data, "th")
        header_content = create_tag("tr", header_content)
        header_content = create_tag("thead", header_content)
        table_data.pop(0)

    content = ""
    #for row in table_data:
#     for i in range(len(table_data)):
#         row = table_data[i]
    for i, row in enumerate(table_data):
        #print(row)
        row_content = ""
        if index:
            row_content = create_tag("td", i+1) 
        row_content += create_row(row, "td")        
        content += create_tag("tr", row_content)
    
    content = create_tag("tbody", content)
    print(create_tag("table", header_content + content))


input = [["lorem", "ipsum"], ["dolor", "sit amet"]]
to_table(input, True, True)