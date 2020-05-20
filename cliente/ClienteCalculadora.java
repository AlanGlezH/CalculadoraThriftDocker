import java.util.Scanner;
import org.apache.thrift.TException;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TTransport;



public class ClienteCalculadora {

    private static Scanner lector;
    private static int numeroUno;
    private static int numeroDos;
    private static Calculadora.Iface cliente;

    public static void main(String[] args) throws TException {

        TTransport transporte = new TSocket("localhost", 8080);
        TProtocol protocolo = new TBinaryProtocol(transporte);
        cliente = new Calculadora.Client(protocolo);
        lector = new Scanner(System.in);
        transporte.open();

       
        int opcion = 0;

        do {
            MostrarMenu();       
            opcion = lector.nextInt();
            lector.nextLine();

            switch (opcion) {
                case 1:
                LeerNumeros("suma");
                MostrarResultado(cliente.Sumar(numeroUno,numeroDos));
                break;

                case 2:
                LeerNumeros("resta");
                MostrarResultado(cliente.Restar(numeroUno,numeroDos));
                break;

                case 3:
                LeerNumeros("multiplicación");
                MostrarResultado(cliente.Multiplicar(numeroUno,numeroDos));
                break;

                case 4:
                LeerNumeros("división");
                MostrarResultado(cliente.Dividir(numeroUno,numeroDos));
                break;

                case -1:
                System.out.println("Saliendo...");
                break;

                default:
                    System.out.println("Ingrese una opción correcta");
                    break;
            }
        } while (opcion != -1);

        transporte.close();


    }


    private static void MostrarMenu(){
        System.out.println("----------Calculadora----------");
        System.out.println("1.Sumar");
        System.out.println("2.Restar");
        System.out.println("3.Multiplicar");
        System.out.println("4.Dividir");
        System.out.println("Ingrese -1 para salir del programa");
        System.out.println("\nSelecciona una opción: ");
    }

    private static void LeerNumeros(String operacion){
        System.out.println("Ingrese el primer numero de la " + operacion + ":");
        numeroUno = lector.nextInt();

        System.out.println("Ingrese el segundo numero de la " + operacion + ":");
        numeroDos = lector.nextInt(); 

        lector.nextLine();

       

        

    }

    private static void MostrarResultado(Resultado resultado){
        if (resultado.mensajeError != null) {
            System.out.println(resultado.mensajeError);
        }

        System.out.println("El resultado es: " + resultado.resultado);
        System.out.println("Presione la tecla enter para continuar");
        lector.nextLine();
        
    
        
    }
}
