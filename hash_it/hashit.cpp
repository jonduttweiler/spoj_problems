//Use c++14 for compile
#include <iostream>
#include <string>
#include <regex>
#include <cstdio>


using namespace std;

bool ocupados[101];
string tHash[101];
int cantC=0;
vector<int> collisions;

int Hash(string key);
void add(string key);
void del(string key);

int main(int argc, char *argv[]) {
   int ncases;
   int noperations;
   string st1,st2,st4;
   cin>>ncases;

   for(int i=0;i<ncases;i++){
	    cin>>noperations;
      getline(cin,st4); //to remove \n at end of number of operations

    for(int j=0;j<noperations;j++){
	     getline(cin,st1,':'); /*leemos la operación*/
	     getline(cin,st2); /*leemos la clave parametro de la operacion*/
       st2 = (string) std::regex_replace( st2, std::regex( "\\s+$" ),""); //clean st2

       if (st2.length() != 0 && (int)(st2[0]) != 32){
	        if(st1[0]=='A') add(st2);
	        else del(st2);
       }
     }

	   cout<<cantC<<"\n";

    for(int k=0;k<101;k++){
      if(ocupados[k]) cout<<k<<':'<<tHash[k]<<"\n";
	   }

    /*reinicializar los arrays y cantC*/
	     cantC=0;
	      for(int l=0;l<101;l++){
          ocupados[l]=0;
	        tHash[l].clear();
	      }
       collisions.clear();
   }
	return 0;
}

int Hash(string key){
 int sum=0;
 for(int i=0;i<key.length();i++)
   sum=sum+(int)key[i]*(i+1);
 return (19*sum)%101;
}

//idx, string
void r_add(int k,string key){
  ocupados[k]=1;
  tHash[k]=key;
  cantC++;
  return;
}

void r_del(int idx){
  ocupados[idx]=0;
  cantC--;
   //if idx belongs to collisions, delete it!
   collisions.erase(std::remove(collisions.begin(), collisions.end(), idx), collisions.end());
  return;
}



void add(string key){
  //cout << "add:"+key+ "\n";;
  int k=Hash(key);

  //# Comprobar que la palabra no sea la misma que algunas de las que causaron colisiones
  for(int x :collisions){
    if (!key.compare(tHash[x])){
      return; //se trata de una palabra que ya esta insertada en otra posicion debido a una colision
    }
  }

  if(!ocupados[k]){
    r_add(k,key);
  } else {
    int c;
    if(!key.compare(tHash[k])){ /*se trata de la misma palabra*/
      return;
    }else{  /*resolver colisión*/
      for(int j=1;j<=19;j++){
        c = ((int)(k+j*j+23*j))%101;
        if(!ocupados[c]) {
          r_add(c,key);
            collisions.push_back(c);
          break;
        }
      }
      return;
    }
  }
}

void del(string key){
  //cout << "delete:"+key + "\n";
  int k;
  k=Hash(key);

  if(ocupados[k]&&!(key.compare(tHash[k]))){ /*encontramos la clave*/
     r_del(k);
 } else { /*buscar a ver si está en otra posición*/
	 int c;
	 for(int j=1;j<=19;j++){
	  c = ((int)(k+j*j+23*j))%101;
	  if(ocupados[c]&&!(key.compare(tHash[c]))){
	      r_del(c);
	      break;
	  }
	 }
	}
}
