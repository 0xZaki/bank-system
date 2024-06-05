# Bank System

## Description

Simple bank system where customer can borrow money with an interest rate and can repay it in one or more transactions

## Analysis

- System should use Decimal for money calculations instead of float to avoid floating point errors
- Customer can borrow money multiple times while already having and outstanding debt

## Edge Cases

- invalid amount of money (negative, zero, not a number)
- invalid interest rate (negative, zero, not a number)
- repaying more than the borrowed amount