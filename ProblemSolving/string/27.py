import textwrap

value = '''   Lorem ipsum   dolor   sit amet,     
 consectetur adipiscing elit. Nullam ut mi velit. Duis pellentesque, nunc lacinia sagittis facilisis, tellus mauris tristique arcu, aliquam elementum nunc magna vitae lorem. Ut lobortis venenatis metus. Nulla vehicula nulla metus, id sollicitudin purus fringilla sit amet. Ut facilisis vitae felis in euismod. Donec sed placerat tortor, sed condimentum ligula. Nullam placerat et augue sit amet feugiat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Vestibulum ex dui, tristique id luctus vitae, tristique non erat. Nam sodales suscipit eros nec iaculis. Duis nec ipsum ut est dictum molestie. Etiam facilisis enim et ultricies elementum. 
            Vivamus condimentum tincidunt semper.    '''

wrapped = textwrap.TextWrapper()
dedented = textwrap.dedent(text=value)
original = wrapped.fill(text=dedented)
print(original)