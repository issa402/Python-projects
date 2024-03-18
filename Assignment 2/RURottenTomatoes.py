def main():
  x = int(input("Enter the number of movies: "))
  y = int(input("Enter the number of reviewers: "))
  ratings = []

  for i in range(x):
      ratings.append([])
      for j in range(y):
          rating = int(input("Enter the rating for movie {} by reviewer {}: ".format(i+1, j+1)))
          ratings[i].append(rating)

  max_sum = 0
  best_movie = 0
  for j in range(y):
      sum_rating = sum(ratings[i][j] for i in range(x))
      if sum_rating > max_sum:
          max_sum = sum_rating
          best_movie = j

  print("The best movie is:", best_movie)

if __name__ == "__main__":
  main()
