package com.hoangvinh.bai2.services;

import com.hoangvinh.bai2.dto.UserCreateRequest;
import com.hoangvinh.bai2.dto.UserResponse;
import com.hoangvinh.bai2.dto.UserUpdateRequest;
import com.hoangvinh.bai2.mappers.UserMapper;
import com.hoangvinh.bai2.model.User;
import com.hoangvinh.bai2.repositories.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.NoSuchElementException;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
    private final UserMapper userMapper;

    public User findUserObjectById(Long id) {
        return userRepository.findById(id).orElseThrow(() -> new NoSuchElementException("User not found"));
    }

    public List<UserResponse> getAllUsers() {
        return userRepository.findAll().stream()
                .map(userMapper::toResponse)
                .toList();
    }

    public UserResponse updateUser(Long id, UserUpdateRequest userUpdateRequest) {
        User user = this.findUserObjectById(id);
        user.setEmail(userUpdateRequest.getEmail());
        user.setUsername(userUpdateRequest.getUsername());
        return userMapper.toResponse(userRepository.save(user));
    }

    public UserResponse findUserById(Long id) {
        User user = this.findUserObjectById(id);
        return userMapper.toResponse(user);
    }

    public UserResponse createUser(UserCreateRequest userCreateRequest) {
        Optional<User> existedUser = userRepository.findByEmail(userCreateRequest.getEmail());
        if (existedUser.isPresent()) {
            throw new DataIntegrityViolationException("Email already exist");
        }
        User user = User.builder()
                .email(userCreateRequest.getEmail())
                .username(userCreateRequest.getUsername())
                .build();
        return userMapper.toResponse(userRepository.save(user));
    }

    public UserResponse deleteUser(Long id) {
        User user = userRepository.findById(id).orElseThrow(NoSuchElementException::new);
        userRepository.delete(user);
        return userMapper.toResponse(user);
    }
}
