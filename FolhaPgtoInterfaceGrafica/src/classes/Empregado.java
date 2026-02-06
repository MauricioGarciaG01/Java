package classes;

public abstract class Empregado extends Pessoa {

    //atributos
    protected String matricula;
    protected double salario;

    public Empregado(String matricula, String nome, String sobrenome, String cpf, Endereco endResidencial) {
        super(nome, sobrenome, cpf, endResidencial);
        this.matricula = matricula;
    }

    public Empregado(String matricula, String nome, String sobrenome, String cpf) {
        super(nome, sobrenome, cpf);
        this.matricula = matricula;
    }

     public double getSalario() {
        return salario;
    }

    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }
    
    protected abstract void calculaSalario();

    public double calculaInss() {
        return getSalario() * 0.08; //taxa de 8%
    }

    public double calculaIR() {
        double ir = 0.;

        if (getSalario() > 1500 && getSalario() <= 2300) {
            ir = getSalario() * 0.15;
        } else if (salario > 2300) {
            ir = getSalario() * 0.27;
        }
        return ir;
    }

    public double calculaSalarioLiquido() {
        return getSalario() - (calculaInss() + calculaIR());
    }

    @Override
    public String dados() {
        java.text.DecimalFormat mascara = new java.text.DecimalFormat("#,##0.00");
        String dadosFunc = "FICHA DE CADASTRO DE " + super.dados() + "\n"
                + "Salário = " + mascara.format(getSalario()) + "\n"
                + "INSS = " + mascara.format(calculaInss()) + "\n"
                + "IRPF = " + mascara.format(calculaIR()) + "\n"
                + "Salário liquido = " + mascara.format(calculaSalarioLiquido());

        return dadosFunc;
    }

}
