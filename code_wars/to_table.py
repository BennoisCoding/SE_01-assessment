def to_table(data, header=False, index=False):
    """Generate an HTML table representing the data from a 2D array."""

    table = "<table>" 

    # Adding a header if header=True.
    if header == True:
        table += "<thead><tr>"

        # Adding empty index if index=True.
        if index == True:
            table += "<th>" + "</th>"

        for header_value in data[0]:
            # Checking if the value is none
            if header_value == None:
                table += "<th>" + "" + "</th>"
            else:
                table += "<th>" + str(header_value) + "</th>"
        table += "</tr></thead>"
        del(data[0])

    table += "<tbody>"

    # Adding body paragraphs.
    for pos, list in enumerate(data):
        table += "<tr>"
        
        # Adding an index if index=True.
        if index == True:
            table += "<td>" + str(pos + 1) + "</td>"

        for value in list:
            # Checking if the value is none
            if value == None:
                table += "<td>" + "" + "</td>"
            else:
                table += "<td>" + str(value) + "</td>"
        table += "</tr>"

    table += "</tbody></table>"

    print(table)


array = [["a", "b", "c", "d", "e"], [True, False, False, True, True]]
to_table(array, True)