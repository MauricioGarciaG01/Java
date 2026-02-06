package classes;

public class Endereco {

    private String logradouro;
    private String numero;
    private String bairro;
    private String cidade;
    private String cep;
    private String uf;

    //Construtores sobrecarregados
    public Endereco() {
    }

    public Endereco(String rua, String numero, String bairro, String cidade, String estado, String cep) {
        this.logradouro = rua;
        this.numero = numero;
        this.bairro = bairro;
        this.cidade = cidade;
        this.uf = estado;
        this.cep = cep;
    }

    public String getBairro() {
        return bairro;
    }

    public void setBairro(String bairro) {
        this.bairro = bairro;
    }

    public String getCep() {
        return cep;
    }

    public void setCep(String cep) {
        this.cep = cep;
    }

    public String getCidade() {
        return cidade;
    }

    public void setCidade(String cidade) {
        this.cidade = cidade;
    }

    public String getUf() {
        return uf;
    }

    public void setUf(String uf) {
        this.uf = uf;
    }

    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public String getLogradouro() {
        return logradouro;
    }

    public void setLogradouro(String logradouro) {
        this.logradouro = logradouro;
    }

   
    public String enderecoCompleto() {
        StringBuilder endereco = new StringBuilder();
        boolean preencheu = false;

        if (logradouro != null && logradouro.trim().length() > 0) {
            endereco.append("\n").append(logradouro);
            preencheu = true;
        }
        if (numero != null && numero.trim().length() > 0) {
            if (preencheu) {
                endereco.append(", ").append(numero);
            }
        }

        if (bairro!= null && !bairro.isEmpty()) {
            endereco.append("\nBairro: ").append(bairro);
        }

        preencheu = false;
        if (cidade!=null && cidade.trim().length() > 0) {
            endereco.append("\n").append(cidade);
            preencheu = true;
        }
        if (uf!= null && uf.trim().length() > 0) {
            if (preencheu) {
                endereco.append(" - ").append(uf);
            } else {
                endereco.append("\n").append(uf);
            }
        }

        if (cep!=null && cep.trim().length() > 0) {
            endereco.append("\nCep: ").append(cep);
        }
        return endereco.toString();
    }

}
