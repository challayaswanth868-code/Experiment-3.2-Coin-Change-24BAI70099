# Experiment 3.2 - Coin Change

## Student Details

Name: Yaswanth  
UID: 24BAI70099  
Subject: CC-II (24CSP-339)

## Problem

Given an array of coin denominations and an amount, find the minimum number of coins required to make the given amount.

Each coin can be used unlimited times.

If the amount cannot be formed, return -1.

## Approach

This problem is solved using Dynamic Programming.

It is an example of the Unbounded Knapsack pattern because each coin denomination can be used any number of times.

Let:

dp[a] = minimum number of coins required to make amount a.

Initialization:

dp[0] = 0

For every amount a and every coin c:

dp[a] = min(dp[a], dp[a-c] + 1)

If dp[amount] remains unreachable, return -1.

## Example

Coins = [1, 2, 5]

Amount = 11

Answer = 3

Because:

11 = 5 + 5 + 1

## Test Cases

| Coins | Amount | Output |
|---|---:|---:|
| [1,2,5] | 11 | 3 |
| [2] | 3 | -1 |
| [1] | 0 | 0 |
| [1,3,4] | 6 | 2 |
| [2,5,10,1] | 27 | 4 |

## Complexity

Time Complexity: O(amount × c)

Space Complexity: O(amount)

where c is the number of coin denominations.

## Key Concept

1-D Dynamic Programming and Unbounded Knapsack.