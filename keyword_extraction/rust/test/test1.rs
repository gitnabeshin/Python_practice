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
