var mongoose = require('mongoose')

var pessoaSchema = new mongoose.Schema({
    _id : {
        type : String,
        required : true,
        alias: ['BI', 'CC']
    },
    nome : String,
    idade : Number,
    sexo : String,
    morada : {
        cidade: String,
        distrito: String
    },
    profissao : String,
    partido_politico : {
        party_abbr: String,
        party_name: String
    },
    religiao : String,
    desportos : [String],
    animais: [String],
    marca_carro : String,
    figura_publica_pt: [String],
    marca_carro : String,
    destinos_favoritos: [String],
    atributos: {
        fumador: Boolean,
        gosta_cinema: Boolean, 
        gosta_viajar: Boolean,
        acorda_cedo: Boolean,
        gosta_ler: Boolean,
        gosta_musica: Boolean,
        gosta_comer: Boolean,
        gosta_animais_estimacao: Boolean,
        gosta_dancar: Boolean,
        comida_favorita: Boolean
    }
}, {versionKey : false})

module.exports = mongoose.model('pessoas', pessoaSchema)