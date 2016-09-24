class CreateUserCharity < ActiveRecord::Migration
  def change
    create_table :user_charities do |t|
      t.belongs_to :user
      t.belongs_to :charity
    end
  end
end
