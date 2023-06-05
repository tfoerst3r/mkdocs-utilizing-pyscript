from mycode.utils import myplot,trans
import matplotlib.pyplot as plt

def translate():
    input = Element("english").element.value
    output = trans(input)
    
    print(f"Input text: {input} -- Output: {output}")

    # output 
    output_div = Element("output")
    output_div.element.innerText = output

def showgraph():

    radius = int(Element("showgraph").element.value)
    print(radius, type(radius))
    theta,r = myplot(radius)

    fig, ax = plt.subplots(
      subplot_kw = {'projection': 'polar'} 
    )
    
    ax.plot(theta, r)
    ax.set_rticks([0.5, 1, 1.5, 2])
    ax.grid(True)

    #pyscript.write('lineplot',fig)
    #display(fig, target="")
    #pyscript.write('lineplot',fig)
    display(fig, target="output")