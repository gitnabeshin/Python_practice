# Rust test func name extraction

## Example of Rust file

```
#[cfg(feature = "parallel")]
pub fn parallel() {
    println!("parallel is enabled");
}

#[cfg(feature = "serde")]
pub fn serde() {
    println!("serde is enabled");
}

// test for feature "special" is enabled / disabled in Cargo.toml
#[cfg(feature = "special")]
pub fn special() {
    println!("special is enabled");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[cfg(feature = "parallel")]
    #[cfg(feature = "serde")]
    #[test]
    fn test_parallel() {
        parallel();
    }

    #[cfg(feature = "serde")]
    #[test]
    fn test_serde() {
        serde();
    }

    #[cfg(feature = "special")]
    #[test]
    fn test_special() {
        special();
    }
}

```

## Run

```
nabeshin@iMacNabeshin keyword_extraction % python3 main.py
List up rust test function in[ ./rust/test/*.rs ]
Completed...
CSV file[ ./out.csv ].
Total  9  functions are listed.
nabeshin@iMacNabeshin keyword_extraction % cat ./out.csv  
No.,file,test_func,feature1,feature2,feature3
1,test1.rs,test_parallel(),parallel,serde,
2,test1.rs,test_serde(),serde,,
3,test1.rs,test_special(),special,,
4,test2.rs,test_parallel(),parallel,serde,special
5,test2.rs,test_serde(),serde,,
6,test2.rs,test_special(),special,,
nabeshin@iMacNabeshin keyword_extraction % 
```