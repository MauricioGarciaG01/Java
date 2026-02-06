package classes;

public class EmpregadoMensalista extends Empregado {
    //atributo

    private String cargo;

    public EmpregadoMensalista(String cargo, String matricula, String nome, String sobrenome, String cpf, Endereco endResidencial) {
        super(matricula, nome, sobrenome, cpf, endResidencial);
        this.cargo = cargo;
         calculaSalario();
    }

    public EmpregadoMensalista(String cargo, String matricula, String nome, String sobrenome, String cpf) {
        super(matricula, nome, sobrenome, cpf);
        this.cargo = cargo;
        calculaSalario();
    }
    
    public String getCargo() {
        return cargo;
    }

    public void setCargo(String cargo) {
        this.cargo = cargo;
        calculaSalario();
    }

    @Override
    protected void calculaSalario() {
        if (cargo.equalsIgnoreCase("Analista de Sistemas")) {
            salario = 3200.;
        } else if (cargo.equalsIgnoreCase("Programador")) {
            salario = 2500.;
        } else if (cargo.equalsIgnoreCase("Administrador de Banco de Dados")) {
            salario = 4000.0;
        } else {
            salario = 0.;
        }
    }

    @Override
    public String dados() {
        return "Empregado Mensalista\n" + super.dados();
    }
}
