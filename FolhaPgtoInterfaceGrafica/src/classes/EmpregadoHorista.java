package classes;

public class EmpregadoHorista extends Empregado {

    //atributos
    private int horasTrab;
    private float valorHoraTrab;

    //Construtor
    public EmpregadoHorista( String matricula, String nome, String sobrenome, String cpf, Endereco endResidencial,int horasTrab, float valorHoraTrab) {
        super(matricula, nome, sobrenome, cpf, endResidencial);
        this.horasTrab = horasTrab;
        this.valorHoraTrab = valorHoraTrab;
        calculaSalario();
    }

    public EmpregadoHorista(String matricula, String nome, String sobrenome, String cpf,int horasTrab, float valorHoraTrab) {
        super(matricula, nome, sobrenome, cpf);
        this.horasTrab = horasTrab;
        this.valorHoraTrab = valorHoraTrab;
        calculaSalario();
    }

    @Override
    protected void calculaSalario() {
        salario = horasTrab * valorHoraTrab;
    }

    public int getHorasTrab() {
        return horasTrab;
    }

    public void setHorasTrab(int horasTrab) {
        this.horasTrab = horasTrab;
        calculaSalario();
    }

    public float getValorHoraTrab() {
        return valorHoraTrab;
    }

    public void setValorHoraTrab(float valorHoraTrab) {
        this.valorHoraTrab = valorHoraTrab;
        calculaSalario();
    }

    @Override
    public String dados() {
        return "Empregado Horista\n"+ super.dados();
    }

}
