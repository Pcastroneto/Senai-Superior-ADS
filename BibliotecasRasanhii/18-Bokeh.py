'''
Bokeh é uma biblioteca para visualização de dados interativa na web. 
Ele permite que os usuários criem visualizações de dados interativas, como gráficos e mapas, que podem  ser incorporados em aplicativos web.
'''

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

# Criando os dados para o gráfico
x = ['A', 'B', 'C', 'D']
y = [10, 20, 30, 40]

# Criando uma fonte de dados para o gráfico
source = ColumnDataSource(data=dict(x=x, y=y))

# Criando o gráfico de barras
p = figure(x_range=x, y_range=(0, max(y)+5), plot_height=300, title="Gráfico de Barras")
p.vbar(x='x', top='y', width=0.9, source=source, line_color='white', fill_color='#3486EB')

# Configurando a aparência do gráfico
p.xgrid.grid_line_color = None
p.y_range.start = 0

# Mostrando o gráfico
show(p)
