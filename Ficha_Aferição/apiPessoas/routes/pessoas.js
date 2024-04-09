var express = require('express');
var router = express.Router();
var Pessoa = require("../controllers/pessoas");
const compositor = require('../models/pessoa');


/* GET users listing. */
router.get('/', function(req, res, next) {
  Pessoa.list(req, res)
    .then(pessoas => {
      res.render('pessoasListPage', { title: 'Pessoas', pessoas: pessoas});
    }).catch(err => {
      res.render('error', { error: err });
    });
});

// get /pessoas/add
router.get('/add', function(req, res, next) {
  res.render('pessoaForm', {title: 'Adicionar entrada'});
});

// GET /pessoas/:id
router.get('/:id', function(req, res, next) {
  Pessoa.findById(req.params.id)
    .then(pessoa => {
      res.render('pessoaPage', {title: 'Informações', pessoa: pessoa});
    }).catch(err => {
      res.render('error', { error: err });
    });
});


module.exports = router;
