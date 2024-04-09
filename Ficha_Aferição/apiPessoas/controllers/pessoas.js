var mongoose = require('mongoose')
const { modelName } = require('../models/pessoa')
var Pessoa = require("../models/pessoa")

module.exports.list = () => {
    return Pessoa 
        .find()
        .sort({nome : 1})
        .exec()
}

module.exports.findById = id => {
    return Compositor 
        .findOne({_id: id})
        .exec()
}

module.exports.findByName = nome => {
    return Compositor 
        .find({nome:nome})
        .exec()
}

// insert 
module.exports.insert = (pessoa) => {
    var newPessoa = new Pessoa(pessoa)
    return newPessoa.save()
}

// update 
module.exports.update = (id, pessoa) => {
    return Pessoa 
        .findByIdAndUpdate(id, compositor, {new : true})
        .exec()
}

// remove 
module.exports.removeById = id => {
    return Pessoa
        .findByIdAndDelete(id)
        .exec()
}

