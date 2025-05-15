var express = require('express')
var app = express()
const logger = (req, res, next) => {
  console.log('Nueva petición HTTP')
  next() // esto es necesario para que la petición continúe
}
app.use(logger)
app.use(express.urlencoded())

app.use(express.static('./public'))
// app.use(express.static(path.join(__dirname, 'public')))

app.get('/:name', (req, res) => {
  // name = req.body.name
  name = req.params.name
  // res.send('<h1>la vida es bella </h1>')
  carros = [1, 2, 3, 4, 54, 5, 6, 65, 4, 3, 23]
  res.render('index', { name: name, title: 'title the pug', message: 'este es un mensaje de los extraterrestes copernicos', carros: carros })
})

app.get('/index', (req, res) => {
  res.send('<h1>la vida es bella con index </h1>')
})

app.post('/users', (req, res) => {
  res.send('users con post ')
})

app.set('view engine', 'pug')
app.set('views', 'views')

app.use((err, req, res, next) => {
  console.log(err.stack)
  // res.status(500).send('algo salió mal ')
  res.status(500).send(err.stack)
})

app.get('/notes/new', (req, res) => {
  res.render('new')
})
app.post('/notes', (req, res) => {
  console.log(req.body)
  res.send('Hola ' + req.body.title)
  // res.render('Hola ' + req.body.name)
})

app.post('/notes', (req, res) => {
  res.render('new')
})

app.listen(3000, () => console.log('listening on por 3000'))
