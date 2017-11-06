package contador;

public class Armazem {
   static int armazenado;
    public int armazem() {
        Contador c1 = new Contador();
        armazenado = c1.contar();
    return armazenado;
    }
    
    
}
