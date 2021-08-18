function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m

# Forward propagation
# Layer 1 is X
X = [ones(m, 1), X];

# This is second layer
z2 = X * Theta1';
a2 = sigmoid(z2);

# Adding bias unit
a2 = [ones(m, 1), a2];

z3 = a2 * Theta2';

# a3 is our hypothesis layer as well
a3 = sigmoid(z3);

# So that each row represents the classifications
recodedY = zeros(m, num_labels);

for i = 1:m
  # For every row of i, index into the i'th column and set that to 1
  recodedY(i, y(i)) = 1;
end


sumForCost = 0;
for i = 1:m
  for j = 1:num_labels
    sumForCost = sumForCost + (-recodedY(i,j)*log(a3(i,j)) - ((1-recodedY(i,j))*log(1-a3(i,j))));
  end
end


# Not really sure how to adjust the amount of times looped for each Theta layer we have...
sumForTheta1 = 0;
for i = 1:size(Theta1,1)
  for j = 2:size(Theta1,2)
    sumForTheta1 = sumForTheta1 + Theta1(i,j)^2;
  end
end

sumForTheta2 = 0;
for i = 1:size(Theta2,1)
  for j = 2:size(Theta2,2)
    sumForTheta2 = sumForTheta2 + Theta2(i,j)^2;
  end
end

regularizationTerm = sumForTheta1 + sumForTheta2;

J = (1/m) * sumForCost;


# Regularizing cost
J = J + (lambda/(2*m)) * regularizationTerm;

%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.

# Theta1_grad and Theta2_grad are the Capital Deltas
# d = small letter delta

for i = 1:m
  # a1 has size of 400x1
  a1 = X(i, :)'; 
  z2 = Theta1 * a1;

  a2 = [1; sigmoid(z2)];
  
  z3 = Theta2 * a2;
  a3 = sigmoid(z3);
  
  recodedY = (([1:num_labels])== y(i))';
  # So it will become something like, for 1 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  
  
  # Finding difference
  delta3 = a3 - recodedY; 
  
  
  # Using the Delta formula, added the bias layer
  delta2 = (Theta2' * delta3) .* [1; sigmoidGradient(z2)];
  
  # Removing the bias layer after calculation
  delta2 = delta2(2:end);
  
  Theta1_grad = Theta1_grad + delta2 * a1';
  Theta2_grad = Theta2_grad + delta3 * a2';
    
end

# Regularization of the gradients
gradTheta1 = (lambda/m) * Theta1(:, 2:end);
gradTheta2 = (lambda/m) * Theta2(:, 2:end);

Theta1_grad = (1/m) * Theta1_grad;
Theta2_grad = (1/m) * Theta2_grad;

Theta1_grad(:, 2:end) = Theta1_grad(:, 2:end) + gradTheta1;

Theta2_grad(:, 2:end) = Theta2_grad(:, 2:end) + gradTheta2;

grad = [Theta1_grad(:); Theta2_grad(:)];
















% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
