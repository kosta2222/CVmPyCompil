/* 
 * File:   main.cpp
 * Author: papa
 *
 * Created on 17 июля 2018 г., 8:33
 */

#include <stdio.h>
#include <stdint.h>
#define DEFAULT_STACK_SIZE      1000
#define DEFAULT_CALL_STACK_SIZE 100
#define DEFAULT_NUM_LOCALS      10
#define EXIT_SUCCESS 0
//опкоды инструкций
typedef enum {
noop=0,
iconst=1,
bipush=2,
iadd=3,
isub=4,
imul=5,
idiv=6,
print=7,
call=8,
ret=9,
stop=10, 
ilt=11,
ieq=12,
br=13,
brt=14,
brf=15,
gload=16,
load=17,
gstore=18,
store=19,
pop=20,
fpush=21 
}VM_CODE;
//started to work at float numbers,stopped
uint32_t unpack754(uint32_t i,unsigned bits,unsigned expbits){
uint32_t result;
int shift;
unsigned bias;
unsigned significandbits=bits-expbits-1;

if (i==0)
 return 0.0;

result=(i&((1L<<significandbits)-1))
result=result/(1L<<significandbits)

result+=1.0f;
bias=(1<<
(expbits-1)
-1);

shift=(
(i>>significandbits)&
(
(1L<<expbits)-1
)
)-bias;
while(shift>0){
result*=2.0;
shift--;}
while(shift<0){
result/=2.0;
shift++;}
result=(1>>(bits-1)) & 1 ? -1.0 : 1.0;
return result;
}
//started to work at float numbers,stopped
#ifdef __cplusplus
extern "C" {
#endif

    /*Заводим структуру чтобы сразу обращатся как Contex-
     * 'кадр' для функции.
     */
    typedef struct {
        int returnip;
        int locals[10];
    } Context;

    typedef struct {
        unsigned char *code;
        int code_size;

        // global variable space
        int *globals;
        int nglobals;

        // Operand stack, grows upwards
        int stack[DEFAULT_STACK_SIZE];
        Context call_stack[DEFAULT_CALL_STACK_SIZE];
    } VM;

    static void vm_context_init(Context *ctx, int ip, int nlocals) {
        if (nlocals > 10) {
            fprintf(stderr, "too many locals requested: %d\n", nlocals);

        }
        ctx->returnip = ip;
    }

    /*
     * Печатаем стек,его count слово элементов
     */
    void vm_print_steck(int *steck, int count) {
        printf("steck=[");
        for (int i = 0; i <= count; i++) {
            printf("%d", steck[i]);
        }
        printf("]\n");
    }

    void vm_init(VM *vm, unsigned char *code, int code_size, int nglobals) {
        vm->code = code;
        vm->code_size = code_size;
        vm->globals = (int*) calloc(nglobals, sizeof (int));
        vm->nglobals = nglobals;
    }

    void vm_free(VM *vm) {
        free(vm->globals);
        free(vm);
    }

    VM *vm_create(unsigned char *code, int code_size, int nglobals) {
        VM *vm = (VM*) calloc(1, sizeof (VM));
        vm_init(vm, code, code_size, nglobals);
        return vm;
    }

#ifdef __cplusplus
}
#endif

unsigned char* readF(const char* filename) {
    unsigned char *cc;
    FILE *fp;
    // чтение из файла
    if ((fp = fopen(filename, "rb")) == NULL) {
        perror("Error occured while opening file");
        exit(2);
    }
    // пока не дойдем до конца, считываем по 256 байт
    while (fread(cc, 1, 256, fp) != NULL) {

    }

    fclose(fp);
    return cc;
}

void vm_exec(VM *vm, int startip, bool trace) {
#define NEXTOP() vm->code[ip++]
#define TARGET_FLOAT(op) \
case op:\
oparg_float=NEXTARG_4_BYTES()
#define TARGET_1ARG(op) \
case op:\
oparg=NEXTARG();
#define TARGET_NOARG(op) \
case op: 
#define DISPATCH() continue 
#define BASIC_PUSH(v)(vm->stack[sp++]=v)
#define BASIC_POP() (vm->stack[--sp])
#define PUSH(v) BASIC_PUSH(v)
#define POP() BASIC_POP() 
#define TOP() (vm->stack[sp-1])
#define SET_TOP(v) (vm->stack[sp-1]=(v))
#define NEXTARG() (ip+=2,vm->code[ip],(vm->code[ip-1]<<8)+vm->code[ip-2])
#define NEXTARG_4_BYTES (ip+=4,vm->code[ip],((vm->code[ip-1]<<8)+(vm->code[ip-2]<<8)+(vm->code[ip-3]<<8)+(vm->code[ip-4])))
    ////регистры
    int ip = 0;
    int opcode = 0;
    int oparg = 0;
    uint32_t oparg_float=0;
    int a, b, x;
    int addr;
    int sp = -1;
    int callsp = -1;
    ip = startip;
    for (;;) {
        opcode = NEXTOP();
        printf("opcode: %d \n", opcode);
        switch (opcode) {

                TARGET_NOARG(iadd) {

                    b = POP();
                    a = TOP();
                    x = a + b;
                    SET_TOP(x);
                    if (x != NULL) DISPATCH();
                    break;
                }

                TARGET_NOARG(isub) {

                    b = POP();
                    a = TOP();
                    x = a - b;
                    SET_TOP(x);
                    if (x != NULL) DISPATCH();
                    break;
                }

                TARGET_NOARG(imul) {

                    b = POP();
                    a = TOP();
                    x = a*b;
                    SET_TOP(x);
                    if (x != NULL) DISPATCH();
                    break;
                }

                TARGET_NOARG(idiv) {

                    b = POP();
                    a = TOP();
                    x = a / b;
                    SET_TOP(x);
                    if (x != NULL) DISPATCH();
                    break;
                }

                TARGET_1ARG(bipush) {
                    PUSH(oparg);
                    printf("oparg: %d", oparg);
                    DISPATCH();
                }
                TARGET_NOARG(fpush){
 
                } 

                TARGET_NOARG(print) {
                    x = TOP();
                    printf("print: %d\n", x);
                    DISPATCH();
                }

                TARGET_NOARG(call) {
                    printf("ip=");
                    addr = NEXTARG(); //индекс 'целевой' функции
                    int nargs = NEXTARG(); //сколько аргументов положили на стек
                    int nlocals = NEXTARG(); //сколько локакальных выделено
                    vm_context_init(&vm->call_stack[callsp], ip, nargs + nlocals);
                    // copy args into new context
                    for (int i = 0; i < nargs; i++) {
                        vm->call_stack[callsp].locals[i] = vm->stack[sp - i];
                    }
                    sp -= nargs;
                    ip = addr; // jump to function
                    DISPATCH();


                }

                TARGET_NOARG(ret) {
                    ip = vm->call_stack[callsp].returnip;
                    callsp--; // pop context
                    break;

                    DISPATCH();
                }
                TARGET_FLOAT(fpush){
                 }

                TARGET_NOARG(stop) {

                    exit(EXIT_SUCCESS);
                }
            default:
            {
                printf("invalid opcode: %d at ip=%d\n", opcode, (ip - 1));
                exit(1);
            }
                vm_print_steck(vm->stack, 100);

        }

    }

}

int main(int argc, char ** argv) {
    //read bin opcodes from code.txt made by antlr py compiller
    unsigned char* code = readF("code.txt");
    //  printf("%d", (int) sizeof (code));
    VM *vm = vm_create(code, sizeof (code), 0);
    vm_exec(vm, 0, false);

    vm_free(vm);
    return 0;
    //In Hex editor
    //12 0A 00 01 02
    //Out:
    /*
      opcode: 18
      opcode: 1
      print: 10
      opcode: 2
     */
}



