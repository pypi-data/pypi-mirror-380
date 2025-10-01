def desmos_graph(expressions,sliders,points,size=[1000,400],axlim=[-10,10,-10,10],font=1):
    import sys
    import io
    import numpy as np
    
    original_screen = sys.stdout
    diagram_html = io.StringIO()
    sys.stdout = diagram_html
    
    hsize = size[0] # horizontal size of graph
    vsize = size[1] # vertical size of graph
    
    lbor = axlim[0] # left border (x-coordinate)
    rbor = axlim[1] # right border (x-coordinate)
    bbor = axlim[2] # bottom border (y-coordinate)
    tbor = axlim[3] # top border (y-coordinate)
 
    indent = '  ' # indentation for html file
    
    print('<script src="https://www.desmos.com/api/v1.11/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6"></script>')
    
    s = '<div id="calculator" style="width: hsizepx; height: vsizepx;"></div>'
    s = s.replace('hsize',str(hsize))
    s = s.replace('vsize',str(vsize))
    print(s) # dimensions
    
    print('<script>') 
    
    print(indent + "var elt = document.getElementById('calculator');")
    print(indent + 'var Calc = Desmos.GraphingCalculator(elt);')
    print()
       
    if expressions != [[]]:
        for exp in expressions:
            s = indent + 'Calc.setExpression({text'
            s = s.replace('text',f"latex:'{exp['latex']}'")
            if 'id' in exp.keys():
                s = s+f", id:'{exp['id']}'"
            if 'color' in exp.keys():
                s = s+f", color:'{exp['color']}'"
            if 'fillOpacity' in exp.keys():
                s = s+f", fillOpacity:'{exp['fillOpacity']}'"
            if 'hidden' in exp.keys():
                s = s+f", hidden:'{exp['hidden']}'"
            s = s + '})'

            print(s)
        print()

    if sliders != [[]]:
        for exp in sliders:
            s = indent + 'Calc.setExpression({text})'
            s = s.replace('text',f"id:'{exp['variable']}', latex:'{exp['variable']}=0'")
            print(s)
            
            s = indent + 'Calc.setExpression({text,sliderBounds:{sliderparams'
            s = s.replace('text',f"id:'{exp['variable']}'")
            if 'min' in exp.keys():
                s = s.replace('sliderparams',f"min:'{exp['min']}'")
            else:
                s = s+f", min:'{exp['min']}'"
            if 'max' in exp.keys():
                s = s+f", max:'{exp['max']}'"
            else:
                s = s+f", max:'{exp['max']}'"
            if 'step' in exp.keys():
                s = s+f", step:'{exp['step']}'"
            else:
                s = s+f", step:'{exp['step']}'"
            s = s + '}})'
            print(s)
        print()

    if points != [[]]:
        for exp in points:
            s = indent + 'Calc.setExpression({text'
            s = s.replace('text',f"latex:'{exp['latex']}'")
            if 'hidden' in exp.keys():
                s = s+f", hidden:'{exp['hidden']}'"
            if 'color' in exp.keys():
                s = s+f", color:'{exp['color']}'"
            if 'label' in exp.keys():
                s = s+f", label:'{exp['label']}'"
            if 'showLabel' in exp.keys():
                s = s+f", showLabel:'{exp['showLabel']}'"
            if 'labelOrientation' in exp.keys():
                s = s+f", labelOrientation:'{exp['labelOrientation']}'"
            if 'labelSize' in exp.keys():
                s = s+f", labelSize:'{exp['labelSize']}'"
            s = s + '})'

            print(s)            
        print()
        
    s = indent + 'Calc.setMathBounds({left:lbor,right:rbor,bottom:bbor,top:tbor})'
    s = s.replace('lbor',str(lbor))
    s = s.replace('rbor',str(rbor))
    s = s.replace('tbor',str(tbor))
    s = s.replace('bbor',str(bbor))
    print(s) # x and y ranges of graph
    
    print(indent + 'Calc.updateSettings({showGrid:true,showXAxis:true,showYAxis:true,lockViewport:true,expressionsCollapsed:true})')
    print('</script>')
    
    sys.stdout = original_screen
    return diagram_html
