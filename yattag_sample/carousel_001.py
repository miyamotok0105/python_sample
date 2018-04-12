from yattag import Doc
from yattag import indent


doc, tag, text, line = Doc().ttl()

def _make_list():
    with tag('ul', id='grocery-list'):
        line('li', 'Tomato sauce', klass="navbar")
        line('li', 'Salt', klass="bg-primary")
        line('li', 'Pepper')

# <header>    
# <div class="navbar navbar-dark bg-dark box-shadow">
#   <div class="container d-flex justify-content-between">
#     <a href="#" class="navbar-brand d-flex align-items-center">
#       <strong>Album</strong>
#     </a>
#   </div>
# </div>
# </header>
def _make_header1():
    with tag("header"):
        doc.stag('div', klass="navbar navbar-dark bg-dark box-shadow")
        with tag("div"):
            text("Album")

# <header>
#   <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
#     <a class="navbar-brand" href="#">Carousel</a>
#     <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
#       <span class="navbar-toggler-icon"></span>
#     </button>
#     <div class="collapse navbar-collapse" id="navbarCollapse">
#       <ul class="navbar-nav mr-auto">
#         <li class="nav-item active">
#           <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
#         </li>
#         <li class="nav-item">
#           <a class="nav-link" href="#">Link</a>
#         </li>
#         <li class="nav-item">
#           <a class="nav-link disabled" href="#">Disabled</a>
#         </li>
#       </ul>
#       <form class="form-inline mt-2 mt-md-0">
#         <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
#         <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
#       </form>
#     </div>
#   </nav>
# </header>

def _make_header2():
    with tag("header"):
        doc.stag('nav', klass="navbar navbar-expand-md navbar-dark fixed-top bg-dark")
        with tag("button", klass="navbar-toggler", type="button"):
            with tag("span", klass="navbar-toggler-icon"):
                text("")
        with tag("div", klass="collapse navbar-collapse", id="navbarCollapse"):
            with tag('ul', klass='navbar-nav mr-auto'):
                #nav-linkでちょっと強調、activeアクティブ
                with tag("li", klass="nav-item nav-link active"):
                    text("Home")
                    with tag("span", klass="sr-only"):
                        text("(current)")
                with tag("li", klass="nav-item nav-link"):
                    text("Link")
                with tag("li", klass="nav-item nav-link"):
                    text("Disabled")


# <div id="myCarousel" class="carousel slide">
#     <ol class="carousel-indicators">
#       <li class="active"></li>
#       <li></li>
#       <li></li>
#     </ol>
#     <div class="carousel-inner">
#       <div class="carousel-item active">
#         <img class="first-slide" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="First slide">
#         <div class="container">
#           <div class="carousel-caption text-left">
#             <h1>Example headline.</h1>
#             <p>Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultricies vehicula ut id elit.</p>
#             <p><a class="btn btn-lg btn-primary" href="#" role="button">Sign up today</a></p>
#           </div>
#         </div>
#       </div>
#     </div>
#     <a class="carousel-control-prev" href="#myCarousel" role="button">
#       <span class="carousel-control-prev-icon"></span>
#     </a>
#     <a class="carousel-control-next" href="#myCarousel" role="button">
#       <span class="carousel-control-next-icon"></span>
#     </a>
# </div>
def _make_slider():
    with tag("div", klass="carousel slide", id="myCarousel"):
        with tag("ol", klass="carousel-indicators"):
            with tag("li", klass="active"):
                text("")
            with tag("li"):
                text("")
            with tag("li"):
                text("")
        with tag("div", klass="carousel-inner"):
            with tag("div", klass="carousel-item active"):
                doc.stag('img', klass="first-slide", src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==", alt="First slide")
                with tag("div", klass="container"):
                    with tag("div", klass="carousel-caption text-left"):
                        line('h1', "Example headline.")
                        line('p', "Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultricies vehicula ut id elit.")
                        with tag("p"):
                            with tag("a", klass="btn btn-lg btn-primary", href="#", role="button"):
                                # text("Sign up today")
                                doc._append('Sign up today')
        with tag("a", klass="carousel-control-prev", role="button"):
            with tag("span", klass="carousel-control-prev-icon"):
                text("")
        with tag("a", klass="carousel-control-next", role="button"):
            with tag("span", klass="carousel-control-next-icon"):
                text("")


def _make_body():
    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('head'):
            #<link rel="stylesheet" href="bootstrap-4.0.0-dist/css/bootstrap.css" type="text/css">
            doc.stag('link', rel="stylesheet", href="./bootstrap-4.0.0-dist/css/bootstrap.css", type="text/css")
            doc.stag('link', rel="stylesheet", href="./styles/carousel.css", type="text/css")

        with tag('body'):
            _make_header2()
            _make_slider()
            text('Hello world!')
            _make_list()


_make_body()


result = indent(
    doc.getvalue(),
    indentation = '    ',
    newline = '\r\n',
    indent_text = True
)
print(result)


f = open('sample.html', 'w')
f.write(result)
f.close()
