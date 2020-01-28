CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    # 定义变量
    declare p int;
    # 变量赋值
    set p=n-1;
RETURN (      
        select ifnull(
                        (
                        # LIMIT a OFFSET b 方法  
                        #select distinct salary from employee order by salary desc limit 1 OFFSET P

                        # LIMIT a,b 方法
                        select distinct salary from employee order by salary desc limit P,1
                        ),null) as SecondHighestSalary 
        );     
END

