class A
  class Realwork_A
    def real_a
      puts "real_a de la clase Realwork_A"      
    end
  end
  class Realwork_B
    def real_b
      puts "ral_b de la clase Realwork_B"      
    end
  end

  def run
      puts "metodo run de la clase A"
  end

end 
  

instanci_de_Realwork_A =  A::Realwork_A.new 

instanci_de_Realwork_A.real_a # =>real_a de la clase Realwork_A

instance_de_Realwork_B = A::Realwork_B.new()
instance_de_Realwork_B.real_b # =>ral_b de la clase Realwork_B

instanci_classe_a = A.new
instanci_classe_a.run # =>metodo run de la clase A
