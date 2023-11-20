isPrime :: Int -> Bool
isPrime num
  | num <= 1 = False
  | otherwise = all (\i -> num `mod` i /= 0) [2..isqrt num]
  where
    isqrt = floor . sqrt . fromIntegral

printPrimes :: Int -> IO ()
printPrimes n = do
  putStrLn $ "Prime numbers between 1 and " ++ show n ++ " are:"
  mapM_ (\i -> when (isPrime i) $ putStr (show i ++ " ")) [2..n]
  putStrLn ""

main :: IO ()
main = do
  putStrLn "Enter n: "
  input <- getLine
  let n = read input :: Int
  printPrimes n
