def create_opening_tag(o_tag):
    """Create opening tag."""
    opening_tag = ""
    opening_tag += f"<{o_tag}>"
    return opening_tag


def create_closing_tag(c_tag):
    """Create closing tag."""
    closing_tag = ""
    closing_tag += f"</{c_tag}>"
    return closing_tag


def create_cell_tags(cell, cell_tag):
    """Create tags for cell."""
    cell_tags = ""
    cell_tags = f"<{cell_tag}>{cell}</{cell_tag}>"
    return cell_tags


def create_index_tags(number, cell_tag):
    """Create index tags for row."""
    index = ""
    index = f"<{cell_tag}>{number}</{cell_tag}>"
    return index


def to_table(data, header=False, index=False):
    """Generate an HTML table representing the data from a 2D array."""

    content = ""

    content += create_opening_tag(o_tag="table")

    # Creating header and deleting header input afterwards.
    if header:
        content += create_opening_tag(o_tag="thead")
        for row in data:
            content += create_opening_tag(o_tag="tr")

            # Checking if index is correct and if so create empty tag.            
            if index:
                    content += create_index_tags(number="", cell_tag="th")

            for cell in row:
                # Checking if cell value is None and create empty string for it.
                if cell == None:
                    content += create_cell_tags(cell="", cell_tag="th")
                else:
                    content += create_cell_tags(cell, cell_tag="th")
            content += create_closing_tag(c_tag="tr")
            content += create_closing_tag(c_tag="thead")
            del(data[0])
            break

    content += create_opening_tag(o_tag="tbody")

    # Creating html table tags for the body.
    for row in data:
        content += create_opening_tag(o_tag="tr")

        # Checking if index is correct and if so create empty tag.
        if index:
            index_number = data.index(row)
            content += create_index_tags((index_number+1), cell_tag="td")

        for cell in row:
            # Checking if cell value is None and create empty string for it.
            if cell == None:
                content += create_cell_tags(cell="", cell_tag="td")
            else:
                content += create_cell_tags(cell, cell_tag="td")
        content += create_closing_tag(c_tag="tr")

        if row == data[-1]:
            content += create_closing_tag(c_tag="tbody")
            content += create_closing_tag(c_tag="table")

    
    print(content)
            
        


input = [["lorem", "ipsum"], ["dolor", "sit amet"]]
to_table(input, True, True)
