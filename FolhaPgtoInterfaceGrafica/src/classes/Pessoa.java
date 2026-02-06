package classes;

public abstract class Pessoa {

    //Atributos
    private String nome, sobrenome, cpf;
    private Endereco endResidencial;

    //Construtor
    public Pessoa(String nome, String sobrenome, String cpf, Endereco endResidencial) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.cpf = cpf;
        this.endResidencial = endResidencial;
    }

    public Pessoa(String nome, String sobrenome, String cpf) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.cpf = cpf;
    }

    //Metodos de Acesso
    public Endereco getEndResidencial() {
        return endResidencial;
    }

    public void setEndResidencial(Endereco endResidencial) {
        this.endResidencial = endResidencial;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSobrenome() {
        return sobrenome;
    }

    public void setSobrenome(String sobrenome) {
        this.sobrenome = sobrenome;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    //Metodos Gerais
    public String nomeCompleto() {
        return getNome() + " " + getSobrenome();
    }

    public String dados() {
        if (getEndResidencial() != null) {
            return nomeCompleto().toUpperCase() + "\n" + "CPF nº " + cpf + "\n"
                    + "Endereço residencial: "
                    + getEndResidencial().enderecoCompleto();

        }

        return nomeCompleto().toUpperCase();
    }

}
